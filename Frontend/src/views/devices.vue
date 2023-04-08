<template>
  <main class="devices-page">
    <span class="material-icons">dashboard</span><span class="title">Devices List</span>
    <router-link :to="{ name: 'NewDevice', params: { service_id: this.id } }" class="float-right">
      <span class="material-icons">add_circle</span>
    </router-link>

    <table class="table">

      <tr>
        <th>Device ID</th>
        <th>Name</th>
        <th>IP</th>
        <th>Service ID</th>
        <th>EDIT/DELETE</th>
        <th>Select</th>
      </tr>


      <tr v-for="item in devices_list" :key="item.device_id">

        <Device :device_id="item.device_id" :name="item.name" :ip="item.ip" :service_id="item.service_id"
          @delete-device="deleteDevice" @edit-device="editDevice" />

      </tr>
    </table>



  </main>
</template>


<script>
import axios from 'axios'
import Device from '../components/Device.vue'
import { API_URL } from '../config.js'

export default {
  name: "devices-page",
  data() {
    return { devices_list: [] }
  }, props: {
    id: {
      type: Number,
      required: true
    },
  },
  created() {
    axios.get(`${API_URL}/devices/services/${this.id}`)
      // axios.get(`${API_URL}/devices/services/2`)
      .then(response => {
        this.devices_list = response.data
      })
      .catch(error => {
        this.devices_list = [];
        console.log(error)
      })
      
  },
  components: { Device },
  methods: {
    deleteDevice(device_id) {
      let index = this.devices_list.findIndex(item => item.id === device_id);
      this.devices_list - page.splice(index, 1);
    },
    editDevice(updatedDevice) {
      let index = this.devices_list.findIndex(item => item.id === updatedDevice.id);
      this.devices_list.splice(index, 1, updatedDevice);
    }
  }

}
</script>

<style>
.title {
  font-size: 40px;
  position: absolute;
  top: 45px;
}

.material-icons {
  color: #4169e1;
  font-size: 70px;

}
</style>