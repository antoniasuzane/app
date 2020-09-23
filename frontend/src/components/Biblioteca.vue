<template>
<!-- eslint-disable max-len -->
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Biblioteca</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.livro-modal>Adicionar Livro</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Título</th>
              <th scope="col">Autor</th>
              <th scope="col">Leu?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(livro, index) in livros" :key="index">
              <td>{{ livro.title }}</td>
              <td>{{ livro.autor }}</td>
              <td>
                <span v-if="livro.read">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.livro-update-modal
                          @click="editLivro(livro)">
                      Alteração
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteLivro(livro)">
                      Excluir
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addLivroModal"
            id="livro-modal"
            title="Adicione um livro"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group"
                    label="Título:"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addLivroForm.title"
                        required
                        placeholder="Enter título">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-autor-group"
                      label="Autor:"
                      label-for="form-autor-input">
            <b-form-input id="form-autor-input"
                          type="text"
                          v-model="addLivroForm.autor"
                          required
                          placeholder="Enter autor">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="addLivroForm.read" id="form-checks">
            <b-form-checkbox value="true">Já leu?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Enviar</b-button>
          <b-button type="reset" variant="danger">Cancelar</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="editLivroModal"
            id="livro-update-modal"
            title="Alterar Livro"
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
        <b-form-group id="form-autor-edit-group"
                      label="Autor:"
                      label-for="form-autor-edit-input">
            <b-form-input id="form-autor-edit-input"
                          type="text"
                          v-model="editForm.autor"
                          required
                          placeholder="Entre com o autor">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-read-edit-group">
          <b-form-checkbox-group v-model="editForm.read" id="form-checks">
            <b-form-checkbox value="true">Já leu?</b-form-checkbox>
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
      livros: [],
      addLivroForm: {
        title: '',
        autor: '',
        read: [],
      },
      message: '',
      showMessage: false,
      editForm: {
        id: '',
        title: '',
        autor: '',
        read: [],
      },
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getLivros() {
      const path = 'http://localhost:5000/biblioteca';
      axios.get(path)
        .then((res) => {
          this.livros = res.data.livros;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    addLivro(payload) {
      const path = 'http://localhost:5000/biblioteca';
      axios.post(path, payload)
        .then(() => {
          this.getLivros();
          this.message = 'Livro adicionado!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getLivros();
        });
    },
    initForm() {
      this.addLivroForm.title = '';
      this.addLivroForm.autor = '';
      this.addLivroForm.read = [];
      this.editForm.id = '';
      this.editForm.title = '';
      this.editForm.autor = '';
      this.editForm.read = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addLivroModal.hide();
      let read = false;
      if (this.addLivroForm.read[0]) read = true;
      const payload = {
        title: this.addLivroForm.title,
        autor: this.addLivroForm.autor,
        read, // property shorthand
      };
      this.addLivro(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addLivroModal.hide();
      this.initForm();
    },
    editLivro(livro) {
      this.editForm = livro;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editLivroModal.hide();
      let read = false;
      if (this.editForm.read[0]) read = true;
      const payload = {
        title: this.editForm.title,
        autor: this.editForm.autor,
        read,
      };
      this.updateLivro(payload, this.editForm.id);
    },
    updateLivro(payload, livroID) {
      const path = `http://localhost:5000/biblioteca/${livroID}`;
      axios.put(path, payload)
        .then(() => {
          this.getLivros();
          this.message = 'Livros alterados!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getLivros();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editLivroModal.hide();
      this.initForm();
      this.getLivros(); // why?
    },
    removeLivro(livroID) {
      const path = `http://localhost:5000/biblioteca/${livroID}`;
      axios.delete(path)
        .then(() => {
          this.getLivros();
          this.message = 'Livro removidos!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getLivros();
        });
    },
    onDeleteLivro(livro) {
      this.removeLivro(livro.id);
    },
  },
  created() {
    this.getLivros();
  },
};
</script>
