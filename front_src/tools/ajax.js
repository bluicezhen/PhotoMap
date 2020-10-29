import axios from 'axios'

/**
 * Send HTTP request
 * @param {string} method       HTTP Status
 * @param {string} url          URL
 * @param {Object} bodyParams   HTTP Body
 * @param {Object} urlParams    URL Params
 * @returns {Promise}
 */
export default function (method, url, { bodyParams = {}, urlParams = {} }) {
  const urlParamList = []
  for (const urlParamsKey in urlParams) {
    urlParamList.push(`${urlParamsKey}=${urlParams[urlParamsKey]}`)
  }
  const urlParamsStr = urlParamList.length === 0 ? '' : (`?${urlParamList.join('&')}`)

  const headers = {}

  if (method === 'post' || method === 'put' || method === 'patch' || method === 'delete') {
    headers['X-CSRFTOKEN'] = getCookie('cloud-stone-bk_csrftoken')
  }

  return axios.request({
    url: `${url}${urlParamsStr}`,
    method,
    headers,
    data: bodyParams,
    withCredentials: true,
  })
}