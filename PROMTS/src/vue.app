<template>
  <div id="app">
    <h1>Calculator</h1>
    <div>
      <input type="number" v-model="num1" placeholder="Enter first number">
      <select v-model="operation">
        <option value="add">+</option>
        <option value="subtract">-</option>
        <option value="multiply">*</option>
        <option value="divide">/</option>
      </select>
      <input type="number" v-model="num2" placeholder="Enter second number">
      <button @click="calculate">Calculate</button>
    </div>
    <p>Result: {{ result }}</p>
    <p v-if="error">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      num1: 0,
      num2: 0,
      operation: 'add',
      result: 0,
      error: '',
    };
  },
  methods: {
    calculate() {
      const data = {
        num1: parseFloat(this.num1),
        num2: parseFloat(this.num2),
        operation: this.operation,
      };

      axios
        .post('http://localhost:5000/calculate', data)
        .then((response) => {
          this.result = response.data.result;
          this.error = '';
        })
        .catch((error) => {
          this.error = error.response.data.error;
        });
    },
  },
};
</script>
