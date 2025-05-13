class ShortcutNavigator {
  constructor(shortcuts = {}, timeout = 1000) {
    this.shortcuts = shortcuts;
    this.buffer   = [];
    this.timeout  = timeout;
    this.clearId  = null;
    this.init();
  }

  init() {
    document.addEventListener('keydown', e => this.onKey(e));
  }

  onKey(event) {
    const key = event.key.toLowerCase();
    if (!/^[a-z0-9]$/.test(key)) return;

    // append to buffer
    this.buffer.push(key);
    clearTimeout(this.clearId);

    // clear buffer after timeout ms of inactivity
    this.clearId = setTimeout(() => { this.buffer = []; }, this.timeout);

    // check each shortcut
    for (const combo in this.shortcuts) {
      const seq = combo.split('+');
      if (this._endsWith(this.buffer, seq)) {
        this.shortcuts[combo]();
        this.buffer = [];     // reset, so you don’t fire it twice
        break;
      }
    }
  }

  _endsWith(buffer, seq) {
    if (seq.length > buffer.length) return false;
    // compare last seq.length elements
    return seq.every((k,i) => buffer[buffer.length - seq.length + i] === k);
  }

  addShortcut(combo, fn) {
    this.shortcuts[combo] = fn;
  }
  removeShortcut(combo) {
    delete this.shortcuts[combo];
  }
}