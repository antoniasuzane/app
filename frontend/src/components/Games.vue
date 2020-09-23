<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Games</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.game-modal>Adicionar Game</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Título</th>
              <th scope="col">Gênero</th>
              <th scope="col">Jogou?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(game, index) in games" :key="index">
              <td>{{ game.title }}</td>
              <td>{{ game.genre }}</td>
              <td>
                <span v-if="game.read">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.game-update-modal
                          @click="editGame(game)">
                      Alteração
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteGame(game)">
                      Excluir
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addGameModal"
            id="game-modal"
            title="Adicione um novo jogo"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group"
                    label="Título:"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addGameForm.title"
                        required
                        placeholder="Enter título">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-genre-group"
                      label="Genre:"
                      label-for="form-genre-input">
            <b-form-input id="form-genre-input"
                          type="text"
                          v-model="addGameForm.genre"
                          required
                          placeholder="Enter genre">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="addGameForm.read" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="editGameModal"
            id="game-update-modal"
            title="Alterar Game"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-title-edit-group"
                    label="Title:"
                    label-for="form-title-edit-input">
          <b-form-input id="form-title-edit-input"
                        type="text"
                        v-model="editForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-genre-edit-group"
                      label="Genre:"
                      label-for="form-genre-edit-input">
            <b-form-input id="form-genre-edit-input"
                          type="text"
                          v-model="editForm.genre"
                          required
                          placeholder="Entre com o gênero">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-read-edit-group">
          <b-form-checkbox-group v-model="editForm.read" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Alterar</b-button>
          <b-button type="reset" variant="danger">Cancelar</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      games: [],
      addGameForm: {
        title: '',
        genre: '',
        read: [],
      },
      message: '',
      showMessage: false,
      editForm: {
        id: '',
        title: '',
        genre: '',
        read: [],
      },
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getGames() {
      const path = 'http://localhost:5000/games';
      axios.get(path)
        .then((res) => {
          this.games = res.data.games;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    addGame(payload) {
      const path = 'http://localhost:5000/games';
      axios.post(path, payload)
        .then(() => {
          this.getGames();
          this.message = 'Game adicionado!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getGames();
        });
    },
    initForm() {
      this.addGameForm.title = '';
      this.addGameForm.genre = '';
      this.addGameForm.read = [];
      this.editForm.id = '';
      this.editForm.title = '';
      this.editForm.genre = '';
      this.editForm.read = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addGameModal.hide();
      let read = false;
      if (this.addGameForm.read[0]) read = true;
      const payload = {
        title: this.addGameForm.title,
        genre: this.addGameForm.genre,
        read, // property shorthand
      };
      this.addGame(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addGameModal.hide();
      this.initForm();
    },
    editGame(game) {
      this.editForm = game;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editGameModal.hide();
      let read = false;
      if (this.editForm.read[0]) read = true;
      const payload = {
        title: this.editForm.title,
        genre: this.editForm.genre,
        read,
      };
      this.updateGame(payload, this.editForm.id);
    },
    updateGame(payload, gameID) {
      const path = `http://localhost:5000/games/${gameID}`;
      axios.put(path, payload)
        .then(() => {
          this.getGames();
          this.message = 'Game updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getGames();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editGameModal.hide();
      this.initForm();
      this.getGames(); // why?
    },
    removeGame(gameID) {
      const path = `http://localhost:5000/games/${gameID}`;
      axios.delete(path)
        .then(() => {
          this.getGames();
          this.message = 'Game removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getGames();
        });
    },
    onDeleteGame(game) {
      this.removeGame(game.id);
    },
  },
  created() {
    this.getGames();
  },
};
</script>
