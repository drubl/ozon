import {Injectable, OnInit} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {CookieService} from 'ngx-cookie-service';

export class AuthLoginData {
  username: string;
  password: string;
}

@Injectable({
  providedIn: 'root'
})

export class AuthService {
  // Проверяем залогинены ли мы
  public isLogin = false;

  private registrationUrl = '/api/register/';

  private logInUrl = '/api/login/';
  private logOutUrl = '/api/logout/';

  constructor(private http: HttpClient,
              private cookieService: CookieService) { }

  checkLoginStatus() {
    const logInStatus = this.cookieService.get('is_login');
    if (logInStatus === 'True') {
      this.isLogin = true;
    } else {
      this.isLogin = false;
    }
  }
  registration(newRegUser) {
    return this.http.post(this.registrationUrl, {
      user: newRegUser
    });
  }
  logIn(logInUser)  {
    return this.http.post(this.logInUrl, logInUser);
  }
  logOut() {
    return this.http.get(this.logOutUrl);
  }
}

