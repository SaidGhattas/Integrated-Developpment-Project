<template>
    <main class="home-page">
  
      <span class="material-icons">dashboard</span><span class="title">Conditions</span>
  
      <div class="dashboard">
        <div class="row">
          <div v-for="item in conditions_list" :key="item.condition_id">
  
            <Condition :name="item.name" :type="item.type" :condition_id="item.condition_id"   />
  
          </div>
        </div>
      </div>
    </main>
  </template>
  
  <script>
  import { createApp } from 'vue'
  import App from '../../src/App.vue'
  import axios from 'axios'
  import Condition from '../components/Condition.vue'
  import { API_URL } from '../config.js'
  
  export default {
    name: "Home",
    props: {
    
    id: {
      type: Number,
      required: true
    },
     rule : {
      type: Object,
      required: true
    }
  },
    data() {
      return { conditions_list: [] }
    },
  
    created() {
  
      axios.get(`${API_URL}/conditions/services/${this.id}`)
        .then(response => {
          this.conditions_list = response.data
        })
        .catch(error => {
          this.conditions_list = [];
          console.log(error)
        })
    },
    components: { Condition },
  
  }
  </script>
  <style lang="scss" scoped>
  .title {
    font-size: 40px;
    margin-left: 10px;
    position: absolute;
    top: 45px;
  }
  
  .material-icons {
    color: #4169e1;
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
  
    .button {
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
    width: 300px;
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