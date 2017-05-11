<template class="body">
  <div class="userdetail">

    <h2 style="text-align: left">{{$route.params.username}}</h2>
    <el-row>
      <router-link :to="{ name: 'index',params:{username:$route.params.username}}"><el-button class="el-button--info el-col-2">返回主界面</el-button></router-link>
      </el-row>
    <el-tabs v-model="activeName2" type="card" @tab-click="tabclick">
      <el-tab-pane label="收益详情" name="first"><h1>收益详情</h1></el-tab-pane>
      <el-tab-pane label="上传记录" name="second"><h1>上传记录</h1></el-tab-pane>
      <el-tab-pane label="更新通告" name="third"><h1>更新通告</h1></el-tab-pane>
    </el-tabs>

    <div v-if="userinfo">
      <el-table
        :data="upload_record"
        border
        style="width: 80%;margin:0 auto">
        <el-table-column type="expand"
        label="图片">
      <template scope="props">
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item label="">
            <img v-bind:src=props.row.image1 style="width: 140px">
            <img v-bind:src=props.row.image2 style="width: 140px">
            <img v-bind:src=props.row.image3 style="width: 140px">
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>
        <el-table-column
          fixed="left"
          prop="date"
          label="日期"
          sortable>
        </el-table-column>
        <el-table-column
          prop="categorys"
          label="大类别">
        </el-table-column>
        <el-table-column
          prop="category"
          label="小类别">
        </el-table-column>
        <el-table-column
          prop="info"
          label="产品名称"
          sortable>
        </el-table-column>
        <el-table-column
          prop="detail"
          label="产品详情"
          sortable>
        </el-table-column>
        <el-table-column
          prop="price"
          label="价格"
          sortable>
        </el-table-column>
      </el-table>
    </div>

  </div>
</template>
<script>
  import axios from "axios";
  import "babel-polyfill";
  import ElButton from "../../node_modules/element-ui/packages/button/src/button";
  import ElForm from "../../node_modules/element-ui/packages/form/src/form";
  export default {
    components: {
      ElForm,
      ElButton},
    name: "userdetail",
    data() {
      return {
        activeName2: 'first',
        order: true,
        userinfo: "",
        ad: "",
        upload_record: "",
      };
    },
    created: function () {
      document.title = "上传记录";
      // -------------------获取上传产品列表------------------
      const formdata = new FormData();
      const vm = this;
      formdata.append("from", "8080");
      formdata.append("user", this.$route.params.username);
      axios.post(this.host_backend+'/backend/get_uploadrecord', formdata,
        {headers: {'Content-Type': 'application/form-data'}, withCredentials: false})
        .then(function (response) {
          const upload_record_ = [];
          if (response.data.status === "200") {
            vm.upload_record = response.data.info.split("}");
            for (let i = 0; i < vm.upload_record.length - 1; i++) {
                const dic = [];
              if (vm.upload_record[i].match(/'image1': <FieldFile: font(\S*)>/)===null){

                }
                if (vm.upload_record[i].match(/'image2': <FieldFile: font(\S*)>/)===null){
                  dic["image1"] = vm.upload_record[i].match(/'image1': <FieldFile: font(\S*)>/)[1];
                }
              if (vm.upload_record[i].match(/'image3': <FieldFile: font(\S*)>/)===null &&
                  vm.upload_record[i].match(/'image2': <FieldFile: font(\S*)>/)!==null){
                    const image1 = vm.upload_record[i].match(/'image1': <FieldFile: font(\S*)>/)[1];
                    const image2 = vm.upload_record[i].match(/'image2': <FieldFile: font(\S*)>/)[1];
                    dic["image1"] = image1;
                    dic["image2"] = image2;
                }
              if (vm.upload_record[i].match(/'image3': <FieldFile: font(\S*)>/)!==null &&
                  vm.upload_record[i].match(/'image2': <FieldFile: font(\S*)>/)!==null &&
                  vm.upload_record[i].match(/'image1': <FieldFile: font(\S*)>/)!==null) {
                    const image1 = vm.upload_record[i].match(/'image1': <FieldFile: font(\S*)>/)[1];
                    const image2 = vm.upload_record[i].match(/'image2': <FieldFile: font(\S*)>/)[1];
                    const image3 = vm.upload_record[i].match(/'image3': <FieldFile: font(\S*)>/)[1];
                    dic["image1"] = image1;
              dic["image2"] = image2;
              dic["image3"] = image3;
                }
              const info = vm.upload_record[i].match(/'info': '(\S*)'/)[1];

              const data = vm.upload_record[i].match(/': '(\S*) 00:/)[1];
              const category = vm.upload_record[i].match(/'category': '(\S*)'/)[1];
              const categorys = vm.upload_record[i].match(/'categorys': '(\S*)'/)[1];
              const price = vm.upload_record[i].match(/'price': (\S*),/)[1];
              const detail = vm.upload_record[i].match(/'detail': '(\S*)'/)[1];
              dic["info"] = info;
              dic["date"] = data;
              dic["category"] = category;
              dic["categorys"] = categorys;
              dic["price"] = price;
              dic["detail"] = detail;
              upload_record_.unshift(dic);
            }
            vm.upload_record = upload_record_;
          }
          else {

          }
        })
        .catch(function (error) {
          alert(error)
        });
    },
    methods: {
      tabclick: function () {
        if (this.activeName2 === "first") {
          this.order = true;
          this.userinfo = "";
          this.ad = ""
        }
        if (this.activeName2 === "second") {
          this.order = "";
          this.userinfo = true;
          this.ad = ""
        }
        if (this.activeName2 === "third") {
          this.order = "";
          this.userinfo = "";
          this.ad = true
        }
      }
    }
  };
</script>
<style>

</style>
