import ajax from './ajax'

export default {
  /**
   * Login Post
   * @param username {string}
   * @param password {string}
   */
  login_post (username, password) {
    return ajax('post', '/api/auth/', { bodyParams: { username, password } })
  }
}
