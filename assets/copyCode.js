document.addEventListener('DOMContentLoaded', () => {
  /* Grab only the *outer* wrapper that always exists */
  document.querySelectorAll('div.highlight').forEach(block => {
    /* Skip if we already added a button (avoids duplicates on hot reload) */
    if (block.dataset.copyBtn) return;
    block.dataset.copyBtn = 'true';

    const btn = document.createElement('button');
    btn.className = 'copy-btn';
    btn.type = 'button';
    btn.setAttribute('aria-label', 'Copy code to clipboard');
    btn.innerHTML = '&#x29C9;&nbsp;Copy';

    /* Absolutely position inside the rounded block */
    block.appendChild(btn);

    btn.addEventListener('click', () => {
      const code = block.querySelector('code').innerText.trim();
      navigator.clipboard.writeText(code).then(() => {
        btn.textContent = 'Copied!';
        setTimeout(() => btn.innerHTML = '&#x29C9;&nbsp;Copy', 3000);
      });
    });
  });
});
