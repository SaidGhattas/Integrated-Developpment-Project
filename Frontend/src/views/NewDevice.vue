<template>
  <main class="new-device">
    <span class="material-icons">add</span><span class="title">New Device</span>
    <div class="dashboard">
      <div class="row">
        <p>Device name: {{ message }}</p>
        <input v-model="name" placeholder="Device" />
        <p>Device IP: {{ message }}</p>
        <input v-model="ip" placeholder="192.168.2.1" />
        <button @click="apply" class="Apply">Apply</button>
      </div>
    </div>
  </main>
</template>
  
<script>
import axios from 'axios'
import { API_URL } from '../config.js'

export default {
  props: {
    service_id: {
      type: Number,
      required: true
    }
  },
  methods: {
    async apply() {
      try {
        let response = await axios.post(`${API_URL}/devices/services/${this.service_id}`,{
        "name": this.name,
        "ip": this.ip,
      });
        console.log(response.data);
      } catch (error) {
        console.error(error);
      }
      this.$router.go(-1)
    },
  },
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
  margin-top: 5px;
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
  margin: 0 10%;
}

.row {
  display: flex;
  flex-direction: row;
  align-items: center;
  position: absolute;

  input {
    background-color: #f1f5f9;
    border-color: #1e293b;
    border: solid 1px;
    padding: 8px 12px;
    font-size: 16px;
    margin-right: 20px;
  }

  p {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    font-size: 24px;
    margin-right: 20px;
    margin-top: 10px;
  }

  .Apply {
    background-color: #4169e1;
    color: #f1f5f9;
    border: none;
    border-radius: 5px;
    padding: 5px;
    margin-left: 10px;
    margin-right: 70px;
    font-size: 16px;
    height: 36px;
    padding: 5px;
  }
}</style>