<template>
  <div id="app">
    <nav class="main-nav">
      <div class="logo">
        <img src="./assets/baby.png" alt="logo" />
      </div>
      <Burger></Burger>
    </nav>

    <Sidebar>
      <ul class="sidebar-panel-nav">
        <li><a href="/about">Graphics</a></li>
        <li><a href="#">Settings</a></li>
        <li>
          <!-- <div class="form-check form-switch">
            <input @click="darkmode()" class="form-check-input" type="checkbox" id="flexSwitchCheckDefault" />
          </div> -->
        </li>
      </ul>
    </Sidebar>
    <router-view />
  </div>
</template>

<script>
import Burger from "./components/menu/Burger";
import Sidebar from "./components/menu/Sidebar";

export default {
  name: "app",
  components: {
    Burger,
    Sidebar,
  },
};
</script>

<style>
html {
  height: 100%;
  overflow: hidden;
}

body {
  border: 0;
  margin: 0;
  padding: 0;
  font-family: "Lato";
  height: 100%;
  background: rgb(255, 255, 255);
  /* background: rgb(101,31,87); */
  /*  background: linear-gradient(45deg, rgba(101,31,87,1) 0%, rgba(225,113,87,1) 48%, rgba(249,248,113,1) 100%); */
}

.logo {
  align-self: center;
  color: #fff;
  font-weight: bold;
  font-family: "Lato";
}

.main-nav {
  display: flex;
  justify-content: space-between;
  padding: 0.5% 0.8%;
}

ul.sidebar-panel-nav {
  list-style-type: none;
}

ul.sidebar-panel-nav > li > a {
  color: #fff;
  text-decoration: none;
  font-size: 150%;
  display: block;
  padding-bottom: 5%;
}
ul.sidebar-panel-nav > li > div > label {
  color: #fff;
  text-decoration: none;
  font-size: 150%;
  display: block;
  padding-bottom: 5%;
}
</style>
