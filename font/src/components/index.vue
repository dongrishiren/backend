<template xmlns:v-on="http://www.w3.org/1999/xhtml">

  <div class="shoes" >
    <link href="../assets/css/bootstrap.min.css">
  <div class="container">
    <div class="jumbotron" style="background: transparent">
      <button  class="btn btn-primary btn-lg" v-on:click="clothes_msg">录入服装信息</button>
      <button  class="btn btn-warning btn-lg" v-on:click="shoes_msg">录入鞋类信息</button>
      <button  class="btn btn-success btn-lg" v-on:click="tools_msg">录入配件信息</button>
    </div>
      <div class="row pull-right">
      <div class="col-md-12">
        <router-link :to="{name:'business_detail',params:{username:$route.params.username}}"  class="glyphicon glyphicon-user" style="font-size: large;color: black"> {{ $route.params.username }}</router-link>
      </div>
      </div>
    <div class="row pull-right">
      <div class="col-md-12">
          <button  class="btn btn-warning btn-sm" v-on:click="logout ">退出</button>
        </div>
      </div>
    </div>


    <div class="container-fluid">
      <div class="row">
        <div class="col-md-4 col-md-offset-4">
          <p style="font-size: x-large">{{ msg }}</p>
          <div class="col-md-6">
            <div class="col-md-6 col-md-offset-8">
              <b>种类</b>
            </div>
          </div>
          <div class="col-md-6">
            <div class="col-md-1 col-md-pull-2">
              <div v-if="shoesselect">

            <select v-model="select_value" >
            <option v-for="category_shoe in categorys_shoes" v-bind:value=category_shoe>{{category_shoe}}</option>
            </select>

              </div>

              <div v-if="clothesselect">
            <select v-model="select_value" >
            <option v-for="category_clothe in categorys_clothes" v-bind:value=category_clothe>{{category_clothe}}</option>
            </select>
              </div>
              <div v-if="toolsselect">
            <select v-model="select_value" >
            <option v-for="category_tool in categorys_tools" v-bind:value=category_tool>{{category_tool}}</option>
            </select>
            </div>
            </div>
            </div>
          <div class="form-group">
            <div class="pull-left"><b>{{head_1}}</b></div>
            <input type="text" class="form-control"  v-model="shoesinfo"  v-bind:placeholder="head_1">
          </div>
          <div class="form-group">
            <div class="pull-left"><b>{{head_2}}</b></div>
            <input type="text" class="form-control"  v-model="shoesdetail"  v-bind:placeholder="head_2">
          </div>
          <div class="form-group">
            <div class="pull-left"><b>价格</b></div>
            <input type="text" class="form-control"  v-model="price"  placeholder="价格">
          </div>
          <div class="form-group">
            <div class="pull-left"><b>上传图片</b></div>
            <input type="file" name="image" v-on:change="get_image" id="image" multiple/>
          </div>
          <button class="btn btn-primary btn-lg" v-on:click="back" type="submit">提交</button>
          <p>{{ info }}</p>
          <p>{{ tip }}</p>

      </div>
    </div>
  </div>
  </div>
</template>


<script>
  import axios from 'axios';
  import "babel-polyfill";
  export default {
    name: 'shoes',
    data(){
        return{
            categorys_shoes:["板鞋","篮球鞋","跑鞋","网鞋","帆布鞋","羽毛球鞋","足球鞋","拖鞋","凉鞋",],
          categorys_clothes:["夏季男装","夏季女装","冬季男装","冬季女装",],
          categorys_tools:["球类配件","袜子","箱包","手脚护腕","眼镜"],
          shoesselect:true,
          clothesselect:"",
          toolsselect:"",
          select_value:"",
              head_1:"鞋类产品信息",
          head_2:"鞋类产品详情",
              msg:"鞋类信息",
              tip: "",
              info: "",
          shoesinfo: "",
          shoesdetail: "",
              price: "",
              images: ""}
          },
      created:function () {
        const vm = this;
          document.title = "运动世界后台系统";
        axios.defaults.withCredentials=true;
        const formdata = new FormData();
        formdata.append("from", "8080");
        axios.post(this.host_backend+'/backend/login_re', formdata, {headers:{"content-type":"", "accept":""}})
          .then(function (response) {
            if (response.data.status === "200") {

            }
            else {
              vm.$router.push({ name: 'login'})
            }
          })
          .catch(function (error) {
            alert(error)
          })
      },
    methods:{
      logout:function () {
        const vm = this;
        const formdata = new FormData();
        formdata.append("from", "8080");
        axios.post(this.host_backend+'/backend/loginout', formdata)
          .then(function (response) {
            if (response.data.status === "200") {
              vm.$router.push({ name: 'login'})
            }
            else {
              alert("未知错误")
            }
          })
          .catch(function (error) {
            alert(error)
          })
      },
      get_image: function (event) {
        this.images = event.target.files;
      },
      shoes_msg: function () {
        this.msg = "鞋类信息";
        this.head_1 = "鞋类产品信息";
        this.head_2 = "鞋类产品详情";
        this.shoesselect = true;
        this.clothesselect = "";
        this.toolsselect = "";
      },
      clothes_msg: function () {
        this.msg = "服装信息";
        this.head_1 = "服装产品信息";
        this.head_2 = "服装产品详情";
        this.shoesselect = "";
        this.clothesselect = true;
        this.toolsselect = "";
      },
      tools_msg: function () {
        this.msg = "配件信息";
        this.head_1 = "配件产品信息";
        this.head_2 = "配件产品详情";
        this.shoesselect = "";
        this.clothesselect = "";
        this.toolsselect = true;
      },

      back: function () {
        const vm = this;
        if(vm.images.length===0){
            alert("图片未上传");
            return
        }
        if (this.images.length>3){
          alert("上传图片数量超过3个，请重新上传！");
          return
        }

        // -----------------储存上传记录--------------------------
        const formdata = new FormData();
        formdata.append("from", "8080");
        formdata.append("info", this.shoesinfo.replace(/\s/g,""));
        formdata.append("detail", this.shoesdetail.replace(/\s/g,""));
        formdata.append("price", this.price.replace(/\s/g,""));
        for(let i=0; i<vm.images.length; i++){
        formdata.append("image"+(i+1).toString(),this.images[i]);
                                }
        formdata.append("category", this.select_value);
        formdata.append("categorys", this.msg.split("信息")[0]);
        formdata.append("user", this.$route.params.username);
        axios.post(this.host_backend+'/backend/save_uploadrecord', formdata,
            {headers: {'Content-Type': 'application/form-data'}, withCredentials:false})
            .then(function (response) {
              if (response.data.status === "200") {
                console.log(JSON.stringify(response.data.info))
              }
              else {
                console.log(JSON.stringify(response.data.info))
              }
            })
            .catch(function (error) {
              alert(error)
            });

        // -----------------储存鞋类信息--------------------------
        if(this.msg === "鞋类信息"){
          const formdata = new FormData();
        formdata.append("shoesinfo", this.shoesinfo.replace(/\s/g,""));
        formdata.append("shoesdetail", this.shoesdetail.replace(/\s/g,""));
        formdata.append("price", this.price.replace(/\s/g,""));
        for(let i=0; i<vm.images.length; i++){
        formdata.append("image"+(i+1).toString(),this.images[i]);
                                }
        formdata.append("category", this.select_value);
        formdata.append("from", "8080");
        formdata.append("user", this.$route.params.username);


          axios.post(this.host_backend+'/backend/shoes_info', formdata,
            {headers: {'Content-Type': 'application/form-data'}})
            .then(function (response) {
              if (response.data.status === "200") {
                vm.tip = JSON.stringify(response.data.info)
              }
              else {
                vm.tip = JSON.stringify(response.data.info)
              }
            })
            .catch(function (error) {
              alert(error)
            });

          axios.post(this.host_business+'/business/get_shoes_info', formdata,
            {headers: {'Content-Type': 'application/form-data'}, withCredentials:false})
            .then(function (response) {
              if (response.data.status === "200") {
                vm.info = JSON.stringify(response.data.tip)
              }
              else {
                vm.info = JSON.stringify(response.data.tip)
              }
            })
            .catch(function (error) {
              alert(error)
            })
        }

        // -----------------储存服装信息--------------------------
        if(this.msg === "服装信息"){
          const formdata = new FormData();
        formdata.append("clothesinfo", this.shoesinfo.replace(/\s/g,""));
        formdata.append("clothesdetail", this.shoesdetail.replace(/\s/g,""));
        formdata.append("price", this.price.replace(/\s/g,""));
                for(let i=0; i<vm.images.length; i++){
        formdata.append("image"+(i+1).toString(),this.images[i]);
                                }
        formdata.append("category", this.select_value);
        formdata.append("from", "8080");
        formdata.append("user", this.$route.params.username);


          axios.post(this.host_backend+'/backend/clothes_info', formdata,
            {headers: {'Content-Type': 'application/form-data'}})
            .then(function (response) {
              if (response.data.status === "200") {
                vm.tip = JSON.stringify(response.data.info)
              }
              else {
                vm.tip = JSON.stringify(response.data.info)
              }
            })
            .catch(function (error) {
              alert(error)
            });

          axios.post(this.host_business+'/business/get_clothes_info', formdata,
            {headers: {'Content-Type': 'application/form-data'}, withCredentials:false})
            .then(function (response) {
              if (response.data.status === "200") {
                vm.info = JSON.stringify(response.data.tip)
              }
              else {
                vm.info = JSON.stringify(response.data.tip)
              }
            })
            .catch(function (error) {
              alert(error)
            })
        }

// -----------------储存配件信息--------------------------
        if(this.msg === "配件信息"){
          const formdata = new FormData();
        formdata.append("toolsinfo", this.shoesinfo.replace(/\s/g,""));
        formdata.append("toolsdetail", this.shoesdetail.replace(/\s/g,""));
        formdata.append("price", this.price.replace(/\s/g,""));
                for(let i=0; i<vm.images.length; i++){
        formdata.append("image"+(i+1).toString(),this.images[i]);
                                }
        formdata.append("category", this.select_value);
        formdata.append("from", "8080");
        formdata.append("user", this.$route.params.username);


          axios.post(this.host_backend+'/backend/tools_info', formdata,
            {headers: {'Content-Type': 'application/form-data'}})
            .then(function (response) {
              if (response.data.status === "200") {
                vm.tip = JSON.stringify(response.data.info)
              }
              else {
                vm.tip = JSON.stringify(response.data.info)
              }
            })
            .catch(function (error) {
              alert(error)
            });

          axios.post(this.host_backend+'/business/get_tools_info', formdata,
            {headers: {'Content-Type': 'application/form-data'},withCredentials:false})
            .then(function (response) {
              if (response.data.status === "200") {
                vm.info = JSON.stringify(response.data.tip)
              }
              else {
                vm.info = JSON.stringify(response.data.tip)
              }
            })
            .catch(function (error) {
              alert(error)
            })
        }

      }
    }
  }

</script>
<style>
  body{background: url(../../static/web_media/back_bg.jpg) no-repeat fixed center;background-size: cover}
</style>
