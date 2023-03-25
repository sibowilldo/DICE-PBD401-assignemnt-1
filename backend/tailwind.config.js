/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js,vue}"],
  theme: {
    extend: {},
  },
  plugins: [
      require('@tailwindcss/forms')],
}
