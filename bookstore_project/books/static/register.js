document.addEventListener('DOMContentLoaded', function() {
    const emailInput = document.getElementById('id_email');
    const usernameInput = document.getElementById('id_username');
    const passwordInput = document.getElementById('id_password1');

    const emailFeedback = document.getElementById('email-feedback');
    const passwordFeedback = document.getElementById('password-feedback');
    const usernameFeedback = document.getElementById('username-feedback');

    // Функция для проверки email по регулярному выражению
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    // Проверка email на лету
    if(emailInput){
      emailInput.addEventListener('keyup', function() {
          const email = emailInput.value;
          if (!validateEmail(email)) {
              emailFeedback.textContent = "Введите корректный email.";
          } else {
              emailFeedback.textContent = "";
              // AJAX-запрос для проверки уникальности email
              fetch(`/books/ajax/check_email/?email=${encodeURIComponent(email)}`)
                  .then(response => response.json())
                  .then(data => {
                      if (data.exists) {
                          emailFeedback.textContent = "Этот email уже используется.";
                      } else {
                          emailFeedback.textContent = "";
                      }
                  })
                  .catch(error => {
                      console.error('Ошибка проверки email:', error);
                  });
          }
      });
    }

    // Проверка длины пароля
    if(passwordInput){
      passwordInput.addEventListener('keyup', function() {
          const password = passwordInput.value;
          if (password.length < 6) {
              passwordFeedback.textContent = "Пароль должен содержать не менее 6 символов.";
          } else {
              passwordFeedback.textContent = "";
          }
      });
    }

    // Проверка для логина
    if(usernameInput){
      usernameInput.addEventListener('keyup', function() {
          if (usernameInput.value.trim() === "") {
              usernameFeedback.textContent = "Логин не может быть пустым.";
          } else {
              usernameFeedback.textContent = "";
          }
      });
    }
});
