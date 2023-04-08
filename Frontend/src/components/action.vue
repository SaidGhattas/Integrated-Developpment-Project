<template>
  
    <div class="cards">
        <div class="items">
                <h3>{{ name }} </h3>
                
                <div>
                    <router-link :to="{ name: 'rules' }"><button class="Apply" @click="apply">Apply</button></router-link>
                </div>
        </div>
    </div>

</template>
<script>
import axios from "axios";
import { ref } from "vue";
import { API_URL } from '../config.js'
export default {
name: "Service",
props: {
    name: {
        type: String,
        required: true
    },
    action_id: {
        type: Number,
        required: true
    }

},
methods: {
    apply() {
      axios.post(`${API_URL}/rules`,{
        action_id:this.action_id,
        condition_id:sessionStorage.getItem("condition_id"),
        condition_value:sessionStorage.getItem("condition_value"),
        condition_type_value:sessionStorage.getItem("condition_type_value"),
        action_device_id:sessionStorage.getItem("action_device_id"),
        condition_device_id:sessionStorage.getItem("condition_device_id"),
      
      }).then(response => {
        console.log(response);
        alert("Rule Added Successfully");
        sessionStorage.clear();
      })
      .catch(error => {
        console.log(error);
        alert("Error");
        sessionStorage.clear();
      });
    }

}
}

</script>
<link rel="stylesheet" href="../style.css">

<style lang="scss" scoped>

.Apply{
background-color: #4169e1;
color: #f1f5f9;
border: none;
border-radius: 5px;
padding: 5px;
margin-left: 10px;
margin-bottom: 10px;
font-size: 16px;
height: 36px;
padding: 5px;
}
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
margin: 0 10%;
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
padding: 0 20px;
font-size: 24px;
flex-direction: column;
width: max-content;
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