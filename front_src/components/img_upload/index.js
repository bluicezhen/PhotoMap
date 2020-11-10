export default {
  name: 'ImgUploadComponent',
  methods: {
    handleFileChange (files) {
      const selectedFiles = document.getElementById('input-upload').files
      for (let i = 0; i < selectedFiles.length; i++) {
        console.log(selectedFiles[i])
      }
    }
  }
}
