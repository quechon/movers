document.addEventListener('DOMContentLoaded', () => {

  document.querySelector('#collapse-button').addEventListener('click', function () {
    this.nextElementSibling.classList.toggle('show');
  })

  document.querySelector('#next-b').addEventListener('click', () => { switchReview('next') })
  document.querySelector('#prev-b').addEventListener('click', () => { switchReview('prev') })
  document.querySelector('button').addEventListener('click', (e) => {

    e.preventDefault();
    validator(document.querySelector('form'))


  })

})

// Function to switch through reviews
let index = 0;

const switchReview = (direction) => {

  if (direction == 'next') {
    index++
  }else if (direction == 'prev') {
    index--
  }

  const slides = document.querySelectorAll('.review')

  if (index > slides.length - 1) {
    index = 0;
  }

  if (index < 0) {
    index = slides.length - 1;
  }

  slides.forEach(element => {
    element.classList.remove('on');
  })

  slides[index].classList.add('on');
}


// Validate form
const validator = (form) => {
  let pass = true
  let v = [];
  let field = form.children;

  // Loop through all inputs inside form
  for (let i = 0; i < field.length; i++) {
    if (field[i].tagName != 'BUTTON') {

      // Validate that fields ARE NOT EMPTY
      if (field[i].value == '' || field[i].value == null) {
        pass = false;
        field[i].style.border = 'solid 1px red';

      }else {
        pass = true
        field[i].style.border = '';

        // Validate Email
        if (field[i].placeholder == 'Email') {
          if (validateEmail(field[i].value) == false) {
            pass = false
            field[i].style.border = 'solid 1px red';
          }
        }
      }

      // For every empty value add the false value to a list
      v.push(pass)
    }
  }

  // If al least one value in list is false return false
  console.log(v)
  v.forEach(valid => {
    if (valid == false) {
      pass = false;
    };
  })

  if (pass != false) pass = true;

  return pass
}

const validateEmail = (email) => {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email)
}
