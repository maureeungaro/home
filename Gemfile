source "https://rubygems.org"

gem "jekyll", "~> 3.10.0"

# This is the default theme for new Jekyll sites. You may change this to anything you like.
gem "minima"
gem "base64"
gem "logger" # Add this proactively to avoid future errors with Ruby 3.5+
gem "csv", require: false
gem "bigdecimal", require: false
gem "webrick", "~> 1.8"


# If you have any plugins, put them here!
# admonitions: [!NOTE], [!TIP], [!WARNING], [!CAUTION], [!IMPORTANT]
group :jekyll_plugins do
	gem "jekyll-feed"
 	gem "jekyll-gfm-admonitions"
	gem "jekyll-toc"
end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
platforms :windows, :jruby do
  gem "tzinfo"
  gem "tzinfo-data"
end

# Performance booster for watching directories on Windows
gem "wdm", platforms: [:windows]

# kramdown v2 ships without the GFM parser by default
gem "kramdown-parser-gfm"

# (Optional) Let MRI/TruffleRuby use newer versions
gem "http_parser.rb", ">= 0.8", platforms: [:ruby, :truffleruby]


# SHELL=/bin/bash
# PATH=/sbin:/bin:/usr/sbin:/usr/bin
# MAILTO=ungaro@jlab.org
# # CUE Machine: ifarm2401
# # .---------------- minute (0 - 59)
# # |  .------------- hour (0 - 23)
# # |  |  .---------- day of month (1 - 31)
# # |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# # |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# # |  |  |  |  |
# # *  *  *  *  * user-name  command to be executed
#
# # this copies the query log from /volatile to the web location
# 01,11,21,31,41,51  *	  *  *  * /home/ungaro/osgLog.sh >/dev/null 2>&1
#

# #!/bin/zsh
#
# src="/volatile/clas12/osg/osgLog.json"
# dest="/u/group/clas/www/gemc/html/web_interface/data/"
# logfile="logs/osgLog.txt"
#
# cp "$src" "$dest"
#
# # recreate the log file with current date/time
# rm -f "$logfile"
# date > "$logfile"