<template>

    <td>{{ condition_name }}</td>
    <td>{{ condition_type_value }}</td>
    <td>{{ condition_value }}</td>
    <td>{{ action_name }}</td>
    <td>
      <button class="btn btn-danger" @click="deleteRule(this.rule_id)">Delete</button>
    </td>
</template>

<script>
import axios from 'axios'
import { API_URL } from '../config.js'


export default {
    name:"Rule",
    props:{
      rule_id:{
        type:Number,
        required:true
      },
      
        action_name:{
            type:String,
            required:true
        },
        action_id:{
        type:Number,
        required:true
      },      
        condition_name:{
            type:String,
            required:true
        },
        condition_id:{
        type:Number,
        required:true
      },
      
      condition_type:{
            type:String,
            required:true
        },
        condition_type_value:{
            type:String,
            required:true
        },
        condition_value:{
            type:Number,
            required:true
        },
       
     
    },
    methods: {
  async deleteRule(ruleId) {
    let response = await axios.delete(`${API_URL}/rules/${ruleId}`)
          .catch(function (error) {
            if (error.response) {
              console.log(error.response.data);
              console.log(error.response.status);
              console.log(error.response.headers);
              return 0;
            }
          });
      if (response) this.$emit('delete-rule', ruleId)
  }
}
}



</script>

<style lang="scss" scoped>

</style>