<template>
   <form method="POST" enctype="multipart/form-data" @submit.prevent="uploadPhoto">
  <label for="photo">Photo:</label>
  <input type="file"  id="photo" name="photo" accept="image/*"><br><br>
  <label for="description">Description:</label>
  <input type="textarea" id="description"><br><br>
  <input type="submit" value="Submit">
</form> 
</template>

<script>
export default {
    data() {
    return {};
    },
    methods:
    {
        uploadPhoto()
        {
            fetch("/api/upload", {method: 'POST'})
                .then(function (response) {
                    return response.json();
                })
            .then(function (data) {
                // display a success message
                console.log(data);
            })
            .catch(function (error) {
                console.log(error);
            });
        }
    }
}
</script>
