import {FormControl} from '@angular/forms';
import {Observable} from 'rxjs';
import {HttpClient} from '@angular/common/http';

// Кастомные валидаторы
export class MyValidators {

  // static uniqEmail(control: FormControl): Promise<{ [key: string]: boolean }> | Observable<{ [key: string]: boolean }> {
  //   return new Promise(resolve => {
  //       if (this.checkMail) {
  //         resolve({
  //           uniqEmail: true
  //         })
  //       } else {
  //         resolve(null);
  //       }
  //   });
  // }
  // static checkMail(control) {
  //   this.http.get(`/api/checkemail/?email=${control.value}`);
  //   return 5;
  // }
}

