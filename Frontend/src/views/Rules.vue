<template>

    <main class="rules-page">

      <span class="material-icons">dashboard</span><span class="title">Rules List</span>
      <table class="table">
     
      <tr>
        <th>Condition</th>
        <th>Condition type value</th>
        <th>Condition value</th>
        <th>Action</th>
        <th>DELETE</th>
      </tr>

    <tr v-for="item in rules_list" :key="item.rule_id">
      <Rule 
        :rule_id="item.rule_id" 
        :action_name="item.action.name" 
        :action_id="item.action.id" 
        :condition_name="item.condition.name" 
        :condition_id="item.condition.id" 
        :condition_type="item.condition.condition_type" 
        :condition_type_value="item.condition_type_value" 
        :condition_value="item.condition_value"
        @delete-rule="deleteRule"
      />

    </tr>
  </table>


</main>
</template>


<script>
import axios from 'axios'
import Rule from '../components/Rule.vue'
import { API_URL } from '../config.js'

export default {
  name: "rules-page",
  data() {
    return { rules_list: [] }
  },
  created() {
    this.getdata();
   
  },
  mounted() {
    this.getdata();
  },
  components: { Rule },
  methods: {
    deleteRule(rule_id) {
      let index = this.rules_list.findIndex(item => item.id === rule_id);
      this.rules_list.splice(index, 1);    
      this.getdata();
    },
    getdata(){
      axios.get(`${API_URL}/rules`)
      .then(response => {
        this.rules_list = response.data
      })
      .catch(error => {
        this.rules_list = [];
        console.log(error)
      })
    },

}


}
</script>

<style>
.title{
    font-size: 40px;
    position: absolute;
    top: 45px;
}
.material-icons {
  color: 	 #4169e1;
    font-size: 70px;

  }
</style>