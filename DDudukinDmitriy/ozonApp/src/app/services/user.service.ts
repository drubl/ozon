import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders, HttpParams} from "@angular/common/http";
import {Observable} from "rxjs";
import {UserData} from "../../User";
import {CookieService} from "ngx-cookie-service";


export class UserLogin {
  username: string
  password: string
}

@Injectable({
  providedIn: 'root'
})
export class UserService {
  public isLogin = this.cookieService.get('is_login');
  public token = this.cookieService.get('csrftoken');
  headersToken = new HttpHeaders({
    'X-CSRFToken': this.token
  });

  constructor(private http: HttpClient, private cookieService: CookieService) {
  }

  public registerUser(user) {
    this.http.post('/api/register/', {user}).subscribe()
  }

  userEntrance(loginAndPassword: UserLogin): Observable<UserLogin> {
    return this.http.post<UserLogin>('/api/login/', loginAndPassword)
  }

  getCustomerData(): Observable<UserData> {
    return this.http.get<UserData>('/api/customer/')
  }

  saveEmail(email) {
    return this.http.put('/api/customer/', email, {
      headers: this.headersToken
    })
  }

  savePhone(phone) {
    return this.http.put('/api/customer/', phone, {
      headers: this.headersToken
    })
  }

  savePersonalData(data) {
    return this.http.put('/api/customer/', data, {
      headers: this.headersToken
    })
  }

  deleteUser() {
    return this.http.delete('/customer/', {
      headers: this.headersToken
    })
  }

  exit() {
    return this.http.get('/api/logout/')
  }
}
