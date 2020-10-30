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
      if (this.loginData.username.length === 0) {
        this.$message.error(`${this.$t('username')}${this.$t('cannot_be_blank')}`)
        return
      }
      if (this.loginData.password.length === 0) {
        this.$message.error(`${this.$t('password')}${this.$t('cannot_be_blank')}`)
        return
      }
      try {
        await this.$backend.login_post(this.loginData.username, this.loginData.password)
        this.$message.success(`${this.$t('login')} ${this.$t('success')}`)
        await this.$router.replace({ path: '/' })
      } catch (e) {
        // pass
      }
    }
  }
}
