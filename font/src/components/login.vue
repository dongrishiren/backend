<template>

  <div class="login">
    <link href="../assets/css/bootstrap.min.css">
<div class="container">
  <div class="row" style="margin-top: 20%">
    <div class="col-md-4 col-md-offset-4 " >

        <h2 class="form-signin-heading">请登录</h2>
        <label for="username" class="sr-only">用户名</label>
        <input type="text" id="username" name="username" class="form-control" v-model="username" placeholder="用户名" >
        <label for="inputPassword" class="sr-only">密码</label>
        <input type="password" id="inputPassword" name="password" class="form-control" v-model="password" placeholder="密码" >
        <div class="checkbox">
          <label>
            <input type="checkbox" value="remember-me">
            记住我 </label>
        </div >
        <button class="btn btn-lg btn-warning btn-block"  v-on:click="fun">登录</button>
          <p style="color: red;font-size: small">{{ info }}</p>
      <router-link to="/regist" style="font-size: small">没有账户，注册一个</router-link>
              </div>

    </div>
  </div>
</div>
</template>

<script>
  import axios from "axios";
  import "babel-polyfill";
  export default {
  name: 'login',
  data () {
    return {
      info:'',
      username: '',
      password: ''
    }
  },
    created: function () {
      document.title = "后台登入";
      const vm = this;
        axios.defaults.withCredentials=true;
        const formdata = new FormData();
        formdata.append("from", "8080");
        axios.post(this.host_backend+'/backend/login_re', formdata, {headers:{"content-type":"", "accept":""}})
          .then(function (response) {
            if (response.data.status === "200") {
              vm.$router.push({ name: 'index',params:{username:response.data.username}})
            }
          })
          .catch(function (error) {
            alert(error)
          })
    },
    methods:{
            fun:function () {
            const vm = this;
                  const formdata = new FormData();
                  formdata.append("username", vm.username);
                  formdata.append("password", vm.password);
                  formdata.append("from", "8080");
                  axios.defaults.withCredentials=true;
              axios.post(this.host_backend+'/backend/back_index', formdata,
                  {headers: {'Content-Type':'application/json'}})
                  .then(function (response) {
                      if (response.data.status==="200"){
                            vm.$router.push({ name: 'index', params: { username: vm.username }})
                      }
                      else {
                        const reg = new RegExp('"', "g");
                          vm.info = JSON.stringify(response.data.error).replace(reg, "");
                      }

                  })
                  .catch(function (error) {
                      alert(error)
                  })
          }
  }
}

</script>
