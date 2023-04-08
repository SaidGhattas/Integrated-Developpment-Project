<template>

  <td>{{ device_id  }}</td>
  <td>{{ name  }}</td>
  <td>{{ ip  }}</td>
  <td>{{ service_id  }}</td>
  <td>
    <router-link :to="{name:'EditDevice',params:{service_id:this.service_id,device_id:this.device_id}}">
    <button class="btn btn-primary" @click="editDevice">Edit</button>
  </router-link>
    <button class="btn btn-danger" @click="deleteDevice(this.device_id)">Delete</button>
  </td>
 

  <td>
    <router-link :to="{name: 'conditions',params:{id:this.service_id,} }">
    <button class="btn btn-success" @click="selected">Select</button>
  </router-link>
  </td>
  </template>
  
  <script>
  import axios from 'axios'
  import { API_URL } from '../config.js'
  export default {
      props:{
        device_id:{
          type:Number,
          required:true
        },
        
          name:{
              type:String,
              required:true
          },
          ip:{
          type:Number,
          required:true
        },      
    
          service_id:{
          type:Number,
          required:true
        },
      },
      data () {
        return {
          rule:""
        }
      },
      created () {
        this.rule="condition_device_id:"+this.device_id;
      },
    methods: {
  editDevice() {
    this.$emit('edit-device', updatedDevice)
  },
  async deleteDevice(deviceId) {
    let response = await axios.delete(`${API_URL}/devices/${deviceId}`)
          .catch(function (error) {
            if (error.response) {
              console.log(error.response.data);
              console.log(error.response.status);
              console.log(error.response.headers);
              return 0;
            }
          });
      if (response) this.$emit('delete-device', deviceId)
  },
  selected() {
    sessionStorage.setItem("condition_device_id",this.device_id);
   
  }}
}
  
  </script>
  
  <style lang="scss" scoped>
  
  </style>