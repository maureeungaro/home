# frozen_string_literal: true

# _plugins/gstring_span.rb
#
# Converts:
#
#   %%G4Box%%
#
# into:
#
#   <span class="gstring">G4Box</span>
#
# Notes:
# - Only runs on Markdown files.
# - Skips fenced code blocks.
# - Skips Liquid raw blocks.
# - Skips inline code spans using backticks.
# - Escapes HTML inside the %%...%% text.
# - Supports escaping a delimiter with \%%.

require "cgi"

module Jekyll
  module GStringSpanPlugin
    PLACEHOLDER_PREFIX = "JekyllGStringSpanProtectedBlock"
    GSTRING_PATTERN = /(?<!\\)%%(.+?)(?<!\\)%%/m.freeze
    ESCAPED_DELIMITER_PATTERN = /\\%%/.freeze

    FENCED_CODE_BLOCK_PATTERN = /
      ^[ \t]*(```+|~~~+).*?$   # opening fence
      .*?
      ^[ \t]*\1[ \t]*$         # matching closing fence
    /mx.freeze

    LIQUID_RAW_BLOCK_PATTERN = /
      \{%\s*raw\s*%\}
      .*?
      \{%\s*endraw\s*%\}
    /mx.freeze

    INLINE_CODE_PATTERN = /(`+)(.+?)\1/m.freeze

    def self.convert(content)
      protected_blocks = []

      content = protect_blocks(content, protected_blocks, LIQUID_RAW_BLOCK_PATTERN)
      content = protect_blocks(content, protected_blocks, FENCED_CODE_BLOCK_PATTERN)

      content = convert_outside_inline_code(content)

      restore_blocks(content, protected_blocks)
    end

    def self.protect_blocks(content, protected_blocks, pattern)
      content.gsub(pattern) do |block|
        key = "#{PLACEHOLDER_PREFIX}#{protected_blocks.length}"
        protected_blocks << block
        key
      end
    end

    def self.restore_blocks(content, protected_blocks)
      protected_blocks.each_with_index do |block, index|
        key = "#{PLACEHOLDER_PREFIX}#{index}"
        content = content.gsub(key, block)
      end

      content
    end

    def self.convert_outside_inline_code(content)
      inline_code_blocks = {}

      without_inline_code = content.gsub(INLINE_CODE_PATTERN) do |inline_code|
        key = "#{PLACEHOLDER_PREFIX}Inline#{inline_code_blocks.length}"
        inline_code_blocks[key] = inline_code
        key
      end

      converted = convert_gstring_spans(without_inline_code)

      inline_code_blocks.each do |key, inline_code|
        converted = converted.gsub(key, inline_code)
      end

      converted
    end

    def self.convert_gstring_spans(content)
      content
        .gsub(GSTRING_PATTERN) do
          text = Regexp.last_match(1)

          # Allow escaped delimiters inside the string:
          # %%literal \%% inside%%
          text = text.gsub(ESCAPED_DELIMITER_PATTERN, "%%")

          %(<span class="gstring">#{CGI.escapeHTML(text)}</span>)
        end
        .gsub(ESCAPED_DELIMITER_PATTERN, "%%")
    end
  end
end

Jekyll::Hooks.register [:pages, :documents], :pre_render do |doc|
  next unless doc.respond_to?(:extname)
  next unless doc.extname.match?(/\.(md|markdown)$/i)

  doc.content = Jekyll::GStringSpanPlugin.convert(doc.content)
end