<template>

  <div class="regist">
    <link href="../assets/css/bootstrap.min.css">
<div class="container">
  <div class="row" style="margin-top: 20%">
    <div class="col-md-4 col-md-offset-4 col-xs-8 col-xs-offset-2">
        <h2 class="form-signin-heading">请注册</h2>
        <input type="text" v-model="username" class="form-control" placeholder="用户名" >
        <input type="password" v-model="password" class="form-control" placeholder="密码" >
        <div class="checkbox">
          <label><input type="checkbox" value="remember-me">记住我 </label>
        </div>
        <button class="btn btn-lg btn-info btn-block" v-on:click="register">注册</button>
          <div class="row">
          <div class="col-md-6 ">
          <p style="color: red;font-size: small">{{ error }}</p><p style="color: green;font-size: small">{{ info }}</p>
              </div>
          <div class="col-md-6 ">
          <router-link to="/" style="font-size: small;color: black">已有账户，直接登入</router-link>
          </div>
          </div>
    </div>
  </div>
</div>
</div>
</template>

<script>
  import axios from "axios";
  import "babel-polyfill";
  export default {
  name: 'regist',
  data () {
    return {
      error:'',
      info: "",
      username: '',
      password: ''
    }
  },
    created: function () {
      document.title = "后台注册"
    },
  methods:{
    register:function () {
      const vm = this;
      axios.defaults.withCredentials = true;
      const formdata = new FormData();
      formdata.append("username", vm.username);
      formdata.append("password", vm.password);
      formdata.append("from", "8080");
                  axios.post(this.host_backend+'/backend/back_register_do', formdata,
                      {headers: {"content-type":"", "accept":""}})
                      .then(function (response) {
                          if (response.data.status==="200"){
                                vm.info = JSON.stringify(response.data.info).replace(new RegExp('"',"g"), "");
                                vm.error = ""
                          }
                          else {
                            const reg = new RegExp('"', "g");
                              vm.error = JSON.stringify(response.data.error).replace(reg, "");
                              vm.info =""
                          }

                      })
                      .catch(function (error) {
                          alert(error)
                      })
              }
  }
}

</script>
