import axios from 'axios'
import getCookie from './get_cookie'

/**
 * Send HTTP request
 * @param {string} method       HTTP Status
 * @param {string} url          URL
 * @param {Object} bodyParams   HTTP Body
 * @param {Object} urlParams    URL Params
 * @returns {Promise}
 */
export default async function (method, url, { bodyParams = {}, urlParams = {} }) {
  const urlParamList = []
  for (const urlParamsKey in urlParams) {
    urlParamList.push(`${urlParamsKey}=${urlParams[urlParamsKey]}`)
  }
  const urlParamsStr = urlParamList.length === 0 ? '' : (`?${urlParamList.join('&')}`)

  const headers = {}
  if (method === 'post' || method === 'put' || method === 'patch' || method === 'delete') {
    headers['X-CSRFTOKEN'] = getCookie('csrftoken')
  }
  try {
    return await axios.request({
      url: `${url}${urlParamsStr}`,
      method,
      headers,
      data: bodyParams,
      withCredentials: true
    })
  } catch (e) {
    console.log('.......', e.response)
    if (e.response.status === 403) {
      console.log('-------- Will turn to login page')
    } else {
      console.log('-------- Will show error message')
    }
  }
}
