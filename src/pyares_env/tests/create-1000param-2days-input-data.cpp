// -*- C++ -*-

#include <cmath>
#include <ctime>
#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>

using std::string;
using std::vector;
using std::cout;

typedef long long int llint;

struct Model {
    double scale;
    double off;
    double delta;
    double a;
    double b;
};

int rand1of2()
{
    return ((rand() % 100) < 50) ? 0 : 1;
}

int rand1of3()
{
    int n = rand() % 300;
    return (n < 100) ? 0 : ((n < 200) ? 1 : 2);
}

int rand1of4()
{
    int m[2][2] = {{0, 1}, {2, 3}};
    return m[rand1of2()][rand1of2()];
}

int randNM(int N, int M)
{
    return ((rand() % N) < M) ? 0 : 1;
}

llint timemsec(time_t s, int msec)
{
    cout << s << '.' << msec << '\n';

    return (s * 1000 + msec);
}

time_t calYMD2TimeStamp(int year, int month, int day,
                        int h, int m, int s)
{
    struct tm tm;

    tm.tm_sec = s;     /* seconds (0 - 60) */
    tm.tm_min = m;     /* minutes (0 - 59) */
    tm.tm_hour = h;    /* hours (0 - 23) */
    tm.tm_mday = day;    /* day of month (1 - 31) */
    tm.tm_mon = month - 1;     /* month of year (0 - 11) */
    tm.tm_year = year - 1900;    /* year - 1900 */

    return timegm(&tm);
}

time_t calYDoY2TimeStamp(int year, int doy,
                        int h, int m, int s)
{
    struct tm tm;

    tm.tm_sec = s;     /* seconds (0 - 60) */
    tm.tm_min = m;     /* minutes (0 - 59) */
    tm.tm_hour = h;    /* hours (0 - 23) */
    tm.tm_yday = doy - 1;    /* day of year (0 - 365) */
    tm.tm_year = year - 1900;    /* year - 1900 */

    return timegm(&tm);
}

double computeParam(Model & model, llint t)
{
    double x = t * 0.001;
    return cos(x/model.a)/(x/model.scale + model.off) + cos(x/model.b)/(model.delta - x/model.scale);
}

string & getParamCateg(vector<string> & categs)
{
    int n;
    switch (categs.size()) {
    case 2:
        n = rand1of2();
        break;
    case 3:
        n = rand1of3();
        break;
    case 4:
        n = rand1of4();
        break;
    default:
        break;
    }
    return categs.at(n);
}

template <class T> T choose(vector<T> & v)
{
    return v.at(rand() % v.size());
}

int main(int argc, char * argv[])
{
    // Start and End time
    llint tstart = timemsec(calYMD2TimeStamp(2014, 1, 1, 0, 0, 0), 0);
    llint tend   = timemsec(calYMD2TimeStamp(2014, 1, 2, 0, 0, 0), 0);

    cout << tstart << " - " << tend << '\n';

    // Template and name holder
    const char tpl[] = "EUCTEST%04d";
    char name[20];
    char date[128];

    // Loop variables
    int msec;
    char msecstr[4];
    time_t sec;
    struct tm tm;

    int rc;

    double value;
    string categ;

    vector<double> offs {1., 2., 3., 4.};
    vector<double> deltas {10., 9., 8., 7., 6.};
    vector<double> as {1000., 2000., 3000.};
    vector<double> bs {4000., 3000., 2000.};

    for (int i = 0; i < 1000; ++i) {

        // Define name
        sprintf(name, tpl, i + 1);

        // Time loop variables
        llint t = tstart;
        llint dt;
        if (i < 400)      { dt = 1000; }
        else if (i < 600) { dt = 5000; }
        else if (i < 800) { dt = 10 * 1000; }
        else if (i < 900) { dt = 60 * 1000; }
        else if (i < 950) { dt = 1800 * 1000; }
        else if (i < 990) { dt = 2 * 3600 * 1000; }
        else              { dt = 86400 * 1000; }

        // Define model
        Model model = { 10000.,
                        choose<double>(offs),
                        choose<double>(deltas),
                        choose<double>(as),
                        choose<double>(bs) };

        bool isCateg = randNM(1000, 100) == 0; // 10% are categorical parameters
        vector<string> categories;

        switch (rand1of4()) {
        case 0:
            categories = vector<string>{"TRUE", "FALSE"};
            break;
        case 1:
            categories = vector<string>{"ON", "OFF"};
            break;
        case 2:
            categories = vector<string>{"INITIALISED", "RUNING", "OPERATIONAL"};
            break;
        case 3:
            categories = vector<string>{"addition", "subtraction", "transposition", "substitution"};
            break;
        }

        do {
            // Get date string
            msec = t % 1000;
            sec = t / 1000;

            gmtime_r(&sec, &tm);
            rc = strftime(date, sizeof(date), "%FT%T.", &tm);
            sprintf(msecstr, "%03d", msec);

            // Gen value
            if (isCateg) {
                categ = choose<string>(categories);
                cout << name << ',' << date << msecstr << ',' << categ << '\n';
            } else {
                value = computeParam(model, t);
                cout << name << ',' << date << msecstr << ',' << value << '\n';
            }

            // Update time
            t += dt;
        } while (t < tend);

        t = tstart;
    }

}
