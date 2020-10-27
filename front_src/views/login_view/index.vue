<template>
  <div class="login-view">
    <div class="form">
        <el-input v-bind:placeholder="$t('username')" class="input"></el-input>
        <el-input v-bind:placeholder="$t('password')" class="input"></el-input>
        <el-button class="input">{{$t('login')}}</el-button>
    </div>
  </div>
</template>

<style lang="scss">
    @import "./index.scss";
</style>
