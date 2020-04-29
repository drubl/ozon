import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {FormControl, FormGroup, Validators} from '@angular/forms';
import {User} from '../../../interfaces';


@Component({
  selector: 'app-modal-page-sign-in',
  templateUrl: './modal-page-sign-in.component.html',
  styleUrls: ['./modal-page-sign-in.component.scss']
})
export class ModalPageSignInComponent implements OnInit {
  @Output() onShowRegHandler: EventEmitter<any> = new EventEmitter<any>();
  form: FormGroup;

  constructor() { }

  ngOnInit() {
    this.form = new FormGroup({
      email: new FormControl(null, [
        Validators.required,
        Validators.email
      ]),
      password: new FormControl(null, [
        Validators.required,
        Validators.minLength(6)
      ])
    });
  }

  submitLogin() {
    if (this.form.invalid) {
      return;
    }
    const user: User = {
      email: this.form.value.email,
      password: this.form.value.password
    };

    console.log(user);
  }

    showModalRegistration() {
        this.onShowRegHandler.emit();
    }
}
