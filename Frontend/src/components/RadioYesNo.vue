<template>
  <div class="input-wrap" >
    <input type="radio" id="yes" name='option' value="yes" v-model="option"  v-bind="$attrs" class="YesNo">
    <label for="yes" class="YesNo">{{labelYes}}</label>
    <input type="radio" id="no" name='option' value="no" v-model="option" v-bind="$attrs" class="YesNo">
    <label for="no" class="YesNo">{{labelNo}}</label>
    <!-- <button @click="save" class="Apply">Apply</button> -->
  </div>
</template>

<script setup> 
defineProps({
  labelYes: {
    type: String,
    default: "Yes",
  },
  labelNo: {
    type: String,
    default: "No",
  },});
</script>

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
  .YesNo{
    margin-left: 10px;
  }
</style>
