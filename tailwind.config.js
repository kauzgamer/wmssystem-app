/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './desktop/templates/**/*.html',
    './mobile/templates/**/*.html',
    './static/js/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          100: '#5a99e6',
          200: '#4a89d6',
          300: '#3a79c6',
          400: '#3570bf',
          500: '#2a60af',
          600: '#244b7e',
          700: '#1e3c66',
          800: '#182e4e',
          900: '#121f36',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
      boxShadow: {
        'soft': '0 4px 6px rgba(0, 0, 0, 0.05), 0 1px 3px rgba(0, 0, 0, 0.1)',
        'inner-soft': 'inset 0 2px 4px 0 rgba(0, 0, 0, 0.06)',
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}