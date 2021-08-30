# vanilla js webpack 설정

1. webpack 설치

   ```shell
   npm init -y
   npm i -D webpack webpack-cli
   ```

   

2. 파일 생성
   html, js, css 파일 만들기

3. webpack.config.js
   웹팩 옵션을 설정하는 파일

   ```javascript
   const path = require("path");
   
   module.exports = {
     entry: "./src/index.js", // 어디를 출발지점으로 번들할지
     output: { // 결과물을 어디로 보낼지
       filename: "bundle.js",
       path: path.resolve(__dirname, "build"),
       clean: true,
     },
   };
   ```

   

4. 빌드

   ```javascript
   npx webpack
   ```

   ```json
    "scripts": {
       "build": "webpack --mode=production",
       "build:dev": "webpack --mode=development"
     },
   ```

   

5. 로더

   ```javascript
   module : {
     rules: {
       test: '가지고올 파일들의 정규식',
       use: [
          {
     	 loader: '사용할 로더의 이름',
     	 options: { 사용할 로더의 옵션 }
          }
       ]
     }
   }
   ```

   다양한 로더를 사용할 수 있다. css-loader, babel-loader 

6. 플러그인

7. 개발서버

   ```javascript
   const path = require('path');
   const HtmlWebpackPlugin = require('html-webpack-plugin');
   
   module.exports = {
     entry: './src/index.js',
     output: {
       filename: 'bundle.js',
       path: path.resolve(__dirname, 'build'),
       clean: true,
     },
     module: {
       rules: [
         {
           test: /\.css$/i,
           use: ['css-loader'],
         },
       ],
     },
     plugins: [new HtmlWebpackPlugin({ template: './src/index.html' })],
     devServer: {
       historyApiFallback: true,
     },
   };

```json
"scripts": {
  "start": "webpack serve --mode=production",
  "start:dev": "webpack serve --mode=development",
  "build": "webpack --mode=production",
  "build:dev": "webpack --mode=production",
},
```

-> npm run start 해보면 디폴트 포트번호인 8080을 사용해 서버가 열리고 'Hello World'를 확인할 수 있다!