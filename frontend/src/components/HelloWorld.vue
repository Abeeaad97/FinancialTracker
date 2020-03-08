<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      For a guide and recipes on how to configure / customize this project,<br>
      check out the
      <a href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</a>.
    </p>
    <h3>Installed CLI Plugins</h3>
    <ul>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel" target="_blank" rel="noopener">babel</a></li>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint" target="_blank" rel="noopener">eslint</a></li>
    </ul>
    <h3>Essential Links</h3>
    <ul>
      <li><a href="https://vuejs.org" target="_blank" rel="noopener">Core Docs</a></li>
      <li><a href="https://forum.vuejs.org" target="_blank" rel="noopener">Forum</a></li>
      <li><a href="https://chat.vuejs.org" target="_blank" rel="noopener">Community Chat</a></li>
      <li><a href="https://twitter.com/vuejs" target="_blank" rel="noopener">Twitter</a></li>
      <li><a href="https://news.vuejs.org" target="_blank" rel="noopener">News</a></li>
    </ul>
    <h3>Ecosystem</h3>
    <ul>
      <li><a href="https://router.vuejs.org" target="_blank" rel="noopener">vue-router</a></li>
      <li><a href="https://vuex.vuejs.org" target="_blank" rel="noopener">vuex</a></li>
      <li><a href="https://github.com/vuejs/vue-devtools#vue-devtools" target="_blank" rel="noopener">vue-devtools</a></li>
      <li><a href="https://vue-loader.vuejs.org" target="_blank" rel="noopener">vue-loader</a></li>
      <li><a href="https://github.com/vuejs/awesome-vue" target="_blank" rel="noopener">awesome-vue</a></li>
    </ul>
  </div>
</template>

<script>
    export default {
        name: 'Home',
        data () {
            return {
                ticker: ''
            }
        },
        methods: {
            getTicker (e) {
                alert(this.ticker)
            }
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->


<style lang="scss" scoped>
    .home {
        display: flex;
        align-items:center;
        justify-content: center;
        height: calc(100vh);

        .input-container{
            max-width: 500px;
            width:100%;

            .input-group{
                display:flex;
                justify-content: space-between;

                input {
                    box-sizing: border-box;
                    width: calc(100% - 150px);
                    padding: .5rem;
                    border: 2px solid cornflowerblue;
                    font-size: 1rem;
                    border-radius: 0;
                    -webkit-appearance: none;
                }

                button{
                    width:150px;
                    height:50px;
                    -webkit-appearance: none;
                    background: cornflowerblue;
                    color: white;
                    text-transform: uppercase;
                    border: none;
                    font-weight:bold;
                    font-size: 12pt;
                }
            }
        }
    }
</style>
