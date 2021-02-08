<template>
  <div id="nav">
    <router-link to="/">Home</router-link>
    <router-link to="/about">About</router-link>
  </div>
  <main>
    <router-view />
  </main>
</template>

<style>
* {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  *, html, body, #app {
    filter: invert(1) !important;
  }
}

html, body {
  margin: 0;
  padding: 0;

  -webkit-touch-callout: none; /* iOS Safari */
      -webkit-user-select: none; /* Safari */
       -khtml-user-select: none; /* Konqueror HTML */
         -moz-user-select: none; /* Old versions of Firefox */
          -ms-user-select: none; /* Internet Explorer/Edge */
              user-select: none; /* Non-prefixed version, currently
                                    supported by Chrome, Edge, Opera and Firefox */
}

a {
  color: blue;
}

button {
  margin: 0;
  padding: 0.5rem;
  padding-left: 0.75rem;
  padding-right: 0.75rem;
  font-family: inherit;
  font-size: inherit;
  color: white;
  background: black;
  border: 1px solid black;
  border: none;
  outline: none;
  cursor: pointer;
}
button:hover {
  background: #333333;
}
button:active {
  background: green;
}
button:focus {
  outline: none;
}

form {
  display: inline-flex;
  flex-flow: column;
  align-items: flex-start;
  justify-content: flex-start;
}

input[type=text] {
  width: 100%;
  margin: 0;
  margin-top: 0.125rem;
  margin-bottom: 0.25rem;
  padding: 0.5rem;
  font-family: inherit;
  font-size: inherit;
  background: gainsboro;
  border: none;
}
input[type=text]:hover {
  background: lightgray;
}
input[type=text]:focus {
  color: white;
  background: dimgray;
  outline: none;
}

#app {
  font-family: sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  line-height: 1.5;
}

main {
  width: 100%;
  max-width: 600px;
  margin: 0;
  margin-left: auto;
  margin-right: auto;
  padding: 0.25rem;
  padding-top: 1rem;
  padding-bottom: 1rem;
}

#nav {
  width: 100%;
  position: sticky;
  top: 0;
  display: inline-flex;
  flex-flow: row;
  align-items: center;
  justify-content: flex-start;
  color: white;
  background: black;
}

#nav a {
  width: 100%;
  max-width: 76px;
  margin: 0;
  padding: 0.5rem;
  padding-left: 1rem;
  padding-right: 1rem;
  font-weight: normal;
  text-align: center;
  text-decoration: none;
  text-overflow: ellipsis;
  overflow: hidden;
  color: white;
  background: none;
}
#nav a:hover {
  background: #333333;
}
#nav a:active,
#nav a.router-link-exact-active {
  color: white;
  background: green;
}
#nav a.router-link-exact-active {
  pointer-events: none;
}
</style>
