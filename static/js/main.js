document.addEventListener('DOMContentLoaded', () => {
  const nav = new ShortcutNavigator({
    'g+l': () => window.location = '/',
    'g+h': () => window.location = '/home'
  });
});