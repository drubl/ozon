import { Injectable } from '@angular/core';
import {AuthService} from '../../../core/auth/auth.service';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs';
import {CookieService} from 'ngx-cookie-service';

export class CustomerInfo {
  birthday: string;
  email: string;
  gender: string;
  id: number;
  name: string;
  password: string | number;
  phone: any;
}

@Injectable({
  providedIn: 'root'
})
export class CustomerService {
  private auth: AuthService;
  private token = this.cookieService.get('csrftoken');
  constructor(auth: AuthService, private http: HttpClient, private cookieService: CookieService) {
  }
  getCustomerInfo(): Observable<CustomerInfo> {
    return this.http.get<CustomerInfo>(`/api/customer/`);
  }
  sendNewMail(newMail) {
    return this.http.put('/api/customer/', {
      email: newMail
    }, {
      headers: new HttpHeaders({
        'X-CSRFToken': this.token
      })
    });
  }
  sendNewPhone(newPhone) {
    return this.http.put('/api/customer/', {
      phone: newPhone
    }, {
      headers: new HttpHeaders({
        'X-CSRFToken': this.token
      })
    });
  }
  sendNewFio(newFio) {
    return this.http.put('/api/customer/', {
      name: newFio
    }, {
      headers: new HttpHeaders({
        'X-CSRFToken': this.token
      })
    });
  }
  sendNewDate(newDate) {
    return this.http.put('/api/customer/', {
      birthday: newDate
    }, {
      headers: new HttpHeaders({
        'X-CSRFToken': this.token
      })
    });
  }
  sendNewGender(newGender) {
    return this.http.put('/api/customer/', {
      gender: newGender
    }, {
      headers: new HttpHeaders({
        'X-CSRFToken': this.token
      })
    });
  }
  deleteProfile() {
    return this.http.delete('/api/customer/',  {
      headers: new HttpHeaders({
        'X-CSRFToken': this.token
      })
    });
  }
}
