import { Component, OnInit } from '@angular/core';
import {FormControl, FormGroup, Validators} from '@angular/forms';
import {MyValidators} from '../../core/validators/myValidators';
import {Observable} from 'rxjs';
import {HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-page-registration',
  templateUrl: './page-registration.component.html',
  styleUrls: ['./page-registration.component.css']
})
export class PageRegistrationComponent implements OnInit {
  form: FormGroup;
  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.form = new FormGroup({
      username: new FormControl('', [
        Validators.required,
        Validators.minLength(4)
      ]),
      password: new FormControl('', [
        Validators.required,
        Validators.minLength(6)
      ]),
      email: new FormControl('', [
        Validators.required,
        Validators.email,
      ], [this.uniqEmail])
    });
  }
  onSubmitForm() {
    console.log('Form submitted ', this.form);
    const formData = {...this.form.value};

    console.log('formData ', formData);
  }


  //
  // if (this.checkMail) {
  // //         resolve({
  // //           uniqEmail: true
  // //         })
  // //       } else {
  // //         resolve(null);
  // //       }
  // Нужно доделать

  uniqEmail(control: FormControl): Promise<{ [key: string]: boolean }> | Observable<{ [key: string]: boolean }> {
      return new Observable(answer => {
        this.checkMail(control.value).subscribe(answer => {
          console.log('работает', answer);
        });
      });
    }
    checkMail(control) {
      return this.http.get(`/api/checkemail/?email=${control}`);
    }
}
