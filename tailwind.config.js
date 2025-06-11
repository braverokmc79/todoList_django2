module.exports = {
  content: [
    "./templates/**/*.html",            // 기본 Django 템플릿
    "./**/templates/**/*.html",         // 앱별 템플릿 포함
  ],
  theme: {
    extend: {
      fontFamily: {
        // 기본 sans 폰트 설정에 나눔고딕과 nosan을 추가
        sans: ['"Nanum Gothic"', 'nosan', 'sans-serif'],
      },
    },
  },
  plugins: [],
}



//npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch