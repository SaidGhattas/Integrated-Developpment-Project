<template>
  <main class="home-page">

    <span class="material-icons">dashboard</span><span class="title">Actions</span>

    <div class="dashboard">
      <div class="row">
        <div v-for="item in ations_list" :key="item.action_id">

          <action :name="item.name" v-model="action" :action_id="item.action_id" />

        </div>
      </div>
    </div>
  </main>
</template>

<script>
import axios from 'axios'
import action from '../components/action.vue'
import { API_URL } from '../config.js'

export default {
  name: "Home",
  props: {

    id: {
      type: Number,
      required: true
    },

  },
  data() {
    return { ations_list: [] }
  },
  created() {

    axios.get(`${API_URL}/actions/services/${this.id}`)
      .then(response => {
        this.ations_list = response.data
      })
      .catch(error => {
        this.ations_list = [];
        console.log(error)
      })
  },

  components: { action },

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
  font-size: 24px;
  flex-direction: column;
  width: 300px;
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