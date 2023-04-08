<template>
    <main class="home-page">
  
      <span class="material-icons">dashboard</span><span class="title">Services Actions</span>
  
      <div class="dashboard">
        <div class="row">
          <div v-for="item in services_list" :key="item.id">
  
            <Service :name="item.name" :type="'action'" :id="item.id" :icon_url="item.icon_url" />
  
          </div>
        </div>
      </div>
    </main>
  </template>

  <script>
  import { createApp } from 'vue'
  import App from '../../src/App.vue'
  import axios from 'axios'
  import Service from '../components/Service.vue'
  import { API_URL } from '../config.js'
  import comparer from "../components/comparer.vue";
  import RadioYesNo from "../components/RadioYesNo.vue";
  export default {
    name: "Home",
    data() {
      return { services_list: [] }
    },
    created() {
  
      axios.get(`${API_URL}/services`)
        .then(response => {
          this.services_list = response.data
        })
        .catch(error => {
          this.services_list = [];
          console.log(error)
        })
    },
    components: { Service },
  
  }
  </script>
<style lang="scss" scoped>
.title{
    font-size: 40px;
    margin-left: 10px;
    position: absolute;
    top: 45px;
}
.material-icons {
  color: 	 #4169e1;
    font-size: 70px;

  }
.dashboard {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 80vh;
  width: 70vw;
}

.row {
  display: flex;
  flex-direction: row;
  .button{
    text-decoration: none;
    color: var(--dark);
  }
}

.cards {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: var(--light);
  border-radius: 10px;
  border: var(--dark) solid 3px;
  margin: 20px;
  font-size: 24px;
  flex-direction: column;
  width:300px;
  height: 230px;
    .items {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        font-size: 24px;
        margin-top: 30px;
        
    }
}
</style>