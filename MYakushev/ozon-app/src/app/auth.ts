import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {CookieService} from 'ngx-cookie-service';

export class AuthId {
  id = 0;
}

@Injectable({
  providedIn: 'root'
})
export class Auth {
  public isLogin = this.cookieService.get('is_login');
  private logInUrl = '/api/login/';
  constructor(private http: HttpClient, private cookieService: CookieService) { }
  public id: number;
  registration(newCustomer) {
    console.log('new Customer: ', newCustomer);
    return this.http.post('/api/register/', {
      user: newCustomer
    });
  }
  login(loginCustomer)  {
    console.log('logIn: ', this.isLogin);
    console.log(loginCustomer);
    this.http.post<AuthId>(this.logInUrl, loginCustomer).subscribe(answer => {
      this.id = answer.id;
    });
    return this.http.post<AuthId>(this.logInUrl, loginCustomer);
  }
  logout() {
    console.log('logOut: ', this.isLogin);
    return this.http.get('api/logout/');
  }
}
