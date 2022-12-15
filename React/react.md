Breve explicación de React:
[How To Use an API with ReactJS](https://rapidapi.com/blog/how-to-use-an-api-with-react/)

<br>

## Conceptos

React es una librerí­a para crear interfaces de usario en ES6 usada en  Single Page Applications, y en móviles con React Native

<img src="https://www.techdiagonal.com/wp-content/uploads/2019/08/React-components-blog-image.jpg">
<br>

Rect sirve para hacer:
 - __componentes__:
    - clases
    - funciones
<br><br>
 - JSX: [babel on line](https://babeljs.io/repl#?browsers=defaults%2C%20not%20ie%2011%2C%20not%20ie_mob%2011&build=&builtIns=false&corejs=3.6&spec=false&loose=false&code_lz=DwEwlgbgfAUABHAEgewDYEM7ABYEYoAKApgA5HAD0esl40QA&debug=false&forceAllTransforms=false&shippedProposals=false&circleciRepo=&evaluate=false&fileSize=false&timeTravel=false&sourceType=module&lineWrap=true&presets=env%2Creact%2Cstage-2&prettier=false&targets=&version=7.20.6&externalPlugins=&assumptions=%7B%7D)



 - [Ciclo de vida de los componentes (en clases)](https://levelup.gitconnected.com/componentdidmakesense-react-lifecycle-explanation-393dcb19e459])

substituido por:
 - hooks (en funciones)

[Understanding React Hooks](https://sst.dev/chapters/understanding-react-hooks.html)

<hr>
<br>

## Api para [{JSON} Placeholder](https://jsonplaceholder.typicode.com/) 

Siguiendo: [How to consume a RESTful API in React](https://pusher.com/tutorials/consume-restful-api-react/)

<br>
Usamos como entorno de desarrollo:

[Vite](https://vitejs.dev/guide/), en lugar del 'oficial'
[create-react-app](https://create-react-app.dev/)

asique:
   
   ```bash
   npm create vite@latest
   ```
que crea el *scalfolding* de la aplicación y tien un servidor de dsarrollo:

   ```bash
   npm run dev
   ```

y un empaquetador para la aplicación de producción:

   ```bash
   npm run build
   ```
<br>
A partir de la versión 18 de React, no se debe usar 
<b>fetch</b> directamente dentro de <b>useEffect</b>,
para traer datos desde una API. Esto se debe a que
useEffect se pasa dos veces durante el desarrollo,
para depurar posibles problemas.

[Data fetching in React 18](https://marcoheine.com/today-i-learned/data-fetching-in-react-18/)

La manera indicada ahora es usar una librería como en
[How to consume a RESTful API in React](https://pusher.com/tutorials/consume-restful-api-react/)


entonces:
   ```bash
   npm i @tanstack/react-query
   ```

y seguimos la página. El código está en
[https://github.com/pusher/react-rest-api-tutorial/tree/with-react-query/src](https://github.com/pusher/react-rest-api-tutorial/tree/with-react-query/src)

<hr>
<br>

## Añdiendo bootstrap

Con [React Bootstrap](https://react-bootstrap.github.io/), una librería de componentes

   ```bash
   npm i react-bootstrap bootstrap
   ```

Hay que añadir las hojas de estilo en **main.jsx**:

   ```jsx
   import 'bootstrap/dist/css/bootstrap.min.css';
   ```
y ya se pueden usar los 
[Componentes](https://react-bootstrap.github.io/components/alerts)

<br>
<hr>
Un resumen: 

[React 101: A beginneres guide to components, state, and props](https://medium.com/@jdimitrop/understanding-react-components-state-and-props-the-building-blocks-of-modern-web-development-634fecb5efb4)

Un poco más despacio: [React JS Crash Course](https://www.youtube.com/watch?v=w7ejDZ8SWv8)