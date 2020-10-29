<template>
  <div class="login-view">
    <div class="form">
        <el-input v-bind:placeholder="$t('username')" class="input" v-model="loginData.username"></el-input>
        <el-input v-bind:placeholder="$t('password')" class="input" v-model="loginData.password"></el-input>
        <el-button class="input" @click="handleChickLogin">{{$t('login')}}</el-button>
    </div>
  </div>
</template>

<script src="./index.js"></script>

<style lang="scss">
    @import "./index.scss";
</style>
