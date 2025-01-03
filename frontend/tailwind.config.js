/** @type {import('tailwindcss').Config} */
/** @type {import('tailwindcss').Config} */

const colors = require('tailwindcss/colors')
export default {
  // Aqui se ingresan los documentos que van a hacer uso de tailwind
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./formkit.config.js",
    "./node_modules/vue-tailwind-datepicker/**/*.js",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {
      colors:{
        "vtd-primary": colors.indigo
      }
    },
  },
  plugins: [
    // require('@tailwindcss/forms')
    require('flowbite/plugin')
  ],
}