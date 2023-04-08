<template>
    <router-link v-if="this.type =='condition'" :to="{name:'devices', params: { id: id}} "   class="button">
      <div class="cards">
        <h3>{{name}}</h3>
        <div class="items">
          <span class="material-icons">{{icon_url}}</span>
        </div>
      </div>
    </router-link>
      <router-link v-else  :to="{name:'deviceActions', params: { id: id}} "   class="button">
        <div class="cards">
          <h3>{{name}}</h3>
          <div class="items">
            <span class="material-icons">{{icon_url}}</span>
          </div>
        </div>
      </router-link>
</template>

<script>
import comparer from "../components/comparer.vue";
import RadioYesNo from "../components/RadioYesNo.vue";
export default {
    name:"Service",
    props:{
        name:{
            type:String,
            required:true
        },
        icon_url:{
            type:String,
            required:true
        },
        id:{
            type:Number,
            required:true
        },

        type:{
            type:String,
            required:true
        }

    },
    created() {
      console.log("name",this.name);
      console.log("type",this.type);
    },
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