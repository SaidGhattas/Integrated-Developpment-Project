<template>
<select v-model="selectedOption"  class="select">
  <option value="GR">></option>
  <option value="GE">>=</option>
  <!-- &lt is the escape character for < in HTML -->
  <option value="LT">&lt</option> 
  <option value="LE">&lt=</option>
  <option value="EQ">=</option>
</select>

  <div class="input-wrap">
    <input
      type="text"
      :value="modelValue"

      @input="$emit('update:modelValue', $event.target.value)"
      v-bind="$attrs"
    />
    
  </div>
  <!-- <button @click="save" class="Apply">Apply</button> -->

</template>

<script setup>
defineProps({
  label: {
    type: [String, Boolean],
    default: false,
  },
  modelValue: {
    type: String,
    default: "",
  },
});

</script>
<script>
export default {
  data() {
    return {
      selectedOption: ''
    }
  },
  watch: {
    selectedOption(selectedValue) {
      this.$emit('option-selected', selectedValue);
    }
  }
}
</script>
<style lang="scss" scoped>
.Apply{
    background-color: #4169e1;
    color: #f1f5f9;
    border: none;
    border-radius: 5px;
    padding: 5px;
    margin-top: 36px;
    font-size: 16px;
    height: 36px;
    padding: 5px;
  }
.input-wrap {
  display: flex;
  flex-direction: column;
  margin: 10px;

  input {
    background-color: #f1f5f9;
    border-color: #1e293b;
    border: solid 1px;
    font-size: 16px;
  }
}
.select{
  background-color: #f1f5f9;
  border-color: #1e293b;
  border: solid 1px;
  font-size: 16px;
  height: 36px;
  align-items: center;
}
</style>