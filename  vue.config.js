const path = require('path')

const customConfig = {
    chainWebpack: (config) => {
        config.entry('app')
            .clear()
            .add('./front_src/main.js')
            .end()
    }
}

module.exports = customConfig