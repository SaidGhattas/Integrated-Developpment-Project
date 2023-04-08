<template>
    <div class="cards">
        <h3>{{ name }}</h3>
        <div class="items">
            <div v-if="type == 'boolean'">
                
                <RadioYesNo v-model="option"  labelYes="YES" labelNo="NO" class="base-input" />
                <router-link :to="{ name: 'ServiceActions'   }"><button class="Apply" @click="apply">Apply</button></router-link>
            </div>
            <div v-else-if="type == 'comparison'" class="d-flex flex-column">
                <div class="d-flex">
                    <comparer v-model="compare" type="Number" @option-selected="onOptionSelected" class="base-input" />
                </div>
                <router-link :to="{ name: 'ServiceActions' }"><button class="Apply" @click="apply">Apply</button></router-link>

            </div>
            <div v-else-if="type == 'timing'">
                <!-- center the labels -->
               
                <label > Every</label><input type="number" v-model="time" class="base-input" />
                <label>Min</label>
                <router-link :to="{ name: 'ServiceActions' }"><button class="Apply" @click="apply">Apply</button></router-link>


            </div>
        </div>
    </div>
</template>
<script>
import comparer from "../components/comparer.vue";
import { ref } from "vue";
import RadioYesNo from "../components/RadioYesNo.vue";


export default {
    name: "Service",
    props: {
        name: {
            type: String,
            required: true
        },
        condition_id: {
            type: Number,
            required: true
        },
        type: {
            type: String,
            required: true
        },
  
    },
    data(){
        return{
        selectedValue:''};
    },
    components: {
        comparer,
        RadioYesNo
    },

    methods: {
        apply() {
            //get value from comparer
            if (this.type == "boolean") {
                sessionStorage.setItem("condition_value", this.option);
                sessionStorage.setItem("condition_type_value", "Detected");
            }
            else if (this.type == "comparison") {
                sessionStorage.setItem("condition_value", this.compare);
            sessionStorage.setItem("condition_type_value", this.selectedValue);

            }
            else if (this.type == "timing") {
                sessionStorage.setItem("condition_value", this.time);
                sessionStorage.setItem("condition_type_value", "Every");

            }
            sessionStorage.setItem("condition_id", this.condition_id);
            
          
            
            
        },
    onOptionSelected(selectedValue) {
      this.selectedValue = selectedValue;
    }
  
    },
}

</script>
<link rel="stylesheet" href="../style.css">

<style lang="scss" scoped>
.Apply {
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