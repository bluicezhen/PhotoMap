export default {
  data () {
    return {
      loginData: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    async handleChickLogin () {
      const res = await this.$backend.login_post(this.loginData.username, this.loginData.password)
      console.log(res)
    }
  }
}
