document.addEventListener('DOMContentLoaded', () => {
  const nav = new ShortcutNavigator({
    'g+l': () => window.location = '/',
    'g+h': () => window.location = '/home',
    'g+s': () => window.location = '/socials',
    'g+p': () => window.location = '/projects',
    'g+b': () => window.location = '/blog',
    'g+a': () => window.location = '/admin',
    'g+g': () => window.scrollTo({top: 0, behavior: 'smooth'}),
    'g+e': () => window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'})
  });
});
